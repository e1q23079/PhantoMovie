import cv2


class Save:
    def __init__(self, filename: str, fps: int, width: int, height: int):
        self.codec = cv2.VideoWriter.fourcc(*"mp4v")  # コーデックの指定
        self.video = cv2.VideoWriter(filename, self.codec, fps, (width, height))

    def save(self, frames):
        """
        Save the given frames to the video file.
        """
        for frame in frames:
            self.write(frame)
        self.release()

    def write(self, frame):
        """
        Save the given frame to the video file.
        """
        self.video.write(frame)

    def release(self):
        """
        Release the video writer.
        """
        self.video.release()
