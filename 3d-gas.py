from manim import *

class TempPlot(ThreeDScene):
  def construct(self):
    axes = ThreeDAxes()

    #plot a function z = x * y
    plot = Surface(
      lambda u, v: np.array([
        u,
        v,
        u * v
      ]), u_range=[-4,4], v_range=[-4,4])

    self.play(Create(axes))
    self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES)
    self.play(Create(plot))
    self.begin_ambient_camera_rotation(rate=0.1)
    self.wait(10)