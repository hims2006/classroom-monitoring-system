"""Frame Streamer for Live Video"""

import asyncio
from typing import Optional


class FrameStreamer:
    """Stream video frames in real-time"""
    
    def __init__(self):
        self.is_streaming = False
        self.frame_queue = asyncio.Queue()
        self.current_status = {
            "is_streaming": False,
            "students_detected": 0,
            "engagement_score": 0,
        }
    
    def start_stream(self):
        """Start streaming"""
        self.is_streaming = True
        self.current_status["is_streaming"] = True
    
    def stop_stream(self):
        """Stop streaming"""
        self.is_streaming = False
        self.current_status["is_streaming"] = False
    
    async def add_frame(self, frame_data: bytes):
        """Add frame to queue"""
        if not self.frame_queue.full():
            await self.frame_queue.put(frame_data)
    
    async def get_frame(self) -> Optional[bytes]:
        """Get frame from queue"""
        try:
            return await asyncio.wait_for(self.frame_queue.get(), timeout=1.0)
        except asyncio.TimeoutError:
            return None
    
    def get_status(self) -> dict:
        """Get streaming status"""
        return self.current_status
    
    def update_metrics(self, students: int, engagement: float):
        """Update metrics"""
        self.current_status["students_detected"] = students
        self.current_status["engagement_score"] = round(engagement, 2)
