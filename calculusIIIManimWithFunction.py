from manim import *

class SurfacePlotWithFunction(ThreeDScene):
    def construct(self):
        # Displaying the function
        function_text = MathTex("z = \\sin(x^2 + y^2)").scale(1.5)
        self.play(Write(function_text))
        self.wait(2)
        self.play(FadeOut(function_text))
        
        # Transition to 3D
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        
        # Define the function
        def func(x, y):
            return np.sin(x**2 + y**2)

        # Create the surface plot
        surface = Surface(
            lambda u, v: np.array([
                u,
                v,
                func(u, v)
            ]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(30, 30),
            color=BLUE
        )
        surface.set_opacity(0.8)
        
        # Animate the surface plot
        self.play(Create(surface))
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.wait()

