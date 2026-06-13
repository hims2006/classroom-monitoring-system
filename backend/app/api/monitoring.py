"""Live Monitoring Endpoints"""

from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session
import json

from app.utils.db import get_db
from app.utils.security import get_current_user
from app.models.user import User
from app.websocket.connection_manager import manager
from app.websocket.frame_streamer import FrameStreamer

router = APIRouter()
frame_streamer = FrameStreamer()


@router.websocket("/ws/live-feed")
async def websocket_live_feed(websocket: WebSocket):
    """WebSocket endpoint for live video feed"""
    await manager.connect(websocket, "live_feed")
    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            
            if message.get("type") == "start":
                await manager.broadcast({
                    "type": "stream_started",
                    "message": "Live feed streaming started"
                })
            elif message.get("type") == "stop":
                await manager.broadcast({
                    "type": "stream_stopped",
                    "message": "Live feed streaming stopped"
                })
    except WebSocketDisconnect:
        await manager.disconnect(websocket, "live_feed")


@router.websocket("/ws/alerts")
async def websocket_alerts(websocket: WebSocket):
    """WebSocket endpoint for real-time alerts"""
    await manager.connect(websocket, "alerts")
    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            await manager.broadcast(message, channel="alerts")
    except WebSocketDisconnect:
        await manager.disconnect(websocket, "alerts")


@router.websocket("/ws/metrics")
async def websocket_metrics(websocket: WebSocket):
    """WebSocket endpoint for real-time metrics"""
    await manager.connect(websocket, "metrics")
    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            await manager.broadcast(message, channel="metrics")
    except WebSocketDisconnect:
        await manager.disconnect(websocket, "metrics")


@router.get("/status")
async def get_monitoring_status(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get current monitoring status"""
    status = frame_streamer.get_status()
    return status
