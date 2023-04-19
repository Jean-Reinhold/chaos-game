import cv2 as cv 
import numpy as np
import random
import imageio
import os


class ChaosGame:
    def __init__(self, num_vertices: int, size: int, num_iterations: int, color: tuple = (255, 255, 255)):
        self.num_vertices = num_vertices
        self.size = size
        self.num_iterations = num_iterations

        self.vertices = self.__generate_vertices()
        self.img = self.__generate_empty_img()
        self.point = self.__pick_starting_point()

        self.color = (255, 255, 255)
    
    def __pick_starting_point(self) -> tuple[int, int]:
        return (random.randint(0, self.size), random.randint(0, self.size))
    
    def __generate_empty_img(self) -> np.array:
        return np.zeros((self.size, self.size, 3), dtype=np.uint8)
    
    def __generate_vertices(self):
        """Generate the vertices of a regular polygon."""
        vertices = []
        for i in range(self.num_vertices):
            angle = i * 2 * np.pi / self.num_vertices
            x = self.size // 2 + int(self.size // 2 * np.cos(angle))
            y = self.size // 2 + int(self.size // 2 * np.sin(angle))
            vertices.append((x, y))
        return vertices
    
    def step(self):
        """Simulate one step of the chaos game and draw a point on the image."""
        vertex = random.choice(self.vertices)
        self.point = ((self.point[0] + vertex[0]) // 2, (self.point[1] + vertex[1]) // 2)
        cv.circle(self.img, self.point, 1, self.color, thickness=-1)
        

def main():
    chaos = ChaosGame(num_vertices=3, size=512, num_iterations=10000)
    frames_dir = 'chaos_frames/'
    if not os.path.exists(frames_dir):
        os.makedirs(frames_dir)
    
    for i in range(chaos.num_iterations):
        chaos.step()
        if i % 50 == 0:
            cv.imwrite(frames_dir + f'{i:05}.png', chaos.img)
    
    frame_files = os.listdir(frames_dir)
    frame_files.sort()
    frames = []
    for file in frame_files:
        frames.append(imageio.imread(frames_dir + file))
    imageio.mimsave('chaos_game.gif', frames, duration=0.05)
    
    for file in frame_files:
        os.remove(frames_dir + file)
    os.rmdir(frames_dir)
        
    cv.imshow('Chaos Game', chaos.img)
    cv.waitKey(0)
    cv.destroyAllWindows()
        

if __name__ == "__main__":
    main()