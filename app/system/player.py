import numpy


class Player:
    def __init__(self, frames: list):
        self.is_playing = False
        self.current_frame_index = 0
        self.frames = frames  # This will hold the frames of the movie

    def get_frame(self) -> tuple[bool, numpy.ndarray | None]:
        if self.current_frame_index < len(self.frames):
            frame = self.frames[self.current_frame_index]
            self.current_frame_index += 1
            return True, frame
        else:
            return False, None

    def play_movie(self):
        # Logic to play the movie
        print("Playing movie...")

    def stop_movie(self):
        # Logic to stop the movie
        print("Stopping movie...")

    def backward_movie(self):
        # Logic to backward the movie
        print("Rewinding movie...")

    def forward_movie(self):
        # Logic to forward the movie
        print("Forwarding movie...")
