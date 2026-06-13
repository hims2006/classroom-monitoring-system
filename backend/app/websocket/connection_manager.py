"""WebSocket Connection Manager"""

from fastapi import WebSocket
from typing import List, Dict
import json


class ConnectionManager:
    """Manage WebSocket connections"""
    
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = {}
    
    async def connect(self, websocket: WebSocket, channel: str):
        """Connect WebSocket"""
        await websocket.accept()
        if channel not in self.active_connections:
            self.active_connections[channel] = []
        self.active_connections[channel].append(websocket)
    
    def disconnect(self, websocket: WebSocket, channel: str):
        """Disconnect WebSocket"""
        if channel in self.active_connections:
            self.active_connections[channel].remove(websocket)
    
    async def broadcast(self, data: dict, channel: str = "default"):
        """Broadcast message to all connected clients"""
        if channel not in self.active_connections:
            return
        
        for connection in self.active_connections[channel]:
            try:
                await connection.send_json(data)
            except Exception as e:
                print(f"Error sending message: {str(e)}")


manager = ConnectionManager()
