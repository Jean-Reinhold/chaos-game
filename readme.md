# Chaos Game Simulation

![Chaos Game](chaos_game.gif)

This is a Python implementation of the Chaos Game simulation using OpenCV. The Chaos Game is a mathematical simulation that generates intricate and beautiful fractal patterns by repeatedly picking a random vertex of a polygon and moving halfway towards it. This implementation allows for customization of the number of vertices, size of the image, number of iterations, and color of the points drawn.

## Requirements

* Python 3.6+
* OpenCV (cv2)
* NumPy

## Usage

To use this implementation, simply run the following command in your terminal:

`python3 chaos_game.py`

This will run the simulation with default parameters, which are:

* Number of vertices: 3
* Size of the image: 512x512
* Number of iterations: 10,000
* Color of the points: white (255, 255, 255)

You can customize the parameters by instantiating a `ChaosGame` object and passing the desired values to its constructor. For example, to create a Chaos Game with 4 vertices, a size of 800x800, 50,000 iterations, and red points, you can do the following:

`chaos = ChaosGame(num_vertices=4, size=800, num_iterations=50000, color=(0, 0, 255))`

After creating a `ChaosGame` object, call its `step` method in a loop to simulate the desired number of iterations. Finally, display the resulting image using OpenCV's `imshow` function and wait for a key press before closing the window:
