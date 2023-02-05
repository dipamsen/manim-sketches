from manim import *


config.pixel_height = 1920
config.pixel_width = 1080

config.frame_width, config.frame_height = config.frame_height, config.frame_width


class Ellipse(Scene):
    def construct(self):
        # create a number plane
        plane = NumberPlane(background_line_style={"stroke_color": GREY}, axis_config={
                            "stroke_color": WHITE}, x_range=[-config.frame_x_radius, config.frame_x_radius], y_range=[-config.frame_y_radius, config.frame_y_radius])

        c1 = Circle(radius=3, color=ORANGE)
        c2 = Circle(radius=1, color=ORANGE)

        angle = ValueTracker(37*DEGREES)
        rotor = Line(ORIGIN, 8 * RIGHT)
        rotor.set_angle(angle.get_value())
        rotor.add_updater(lambda m: m.set_angle(angle.get_value()))

        p1 = Dot(np.cos(angle.get_value()) * RIGHT + np.sin(angle.get_value()) * UP).add_updater(lambda m: m.move_to(
            np.cos(angle.get_value()) * RIGHT + np.sin(angle.get_value()) * UP))
        p2 = Dot(3 * np.cos(angle.get_value()) * RIGHT + 3 * np.sin(angle.get_value()) * UP).add_updater(lambda m: m.move_to(
            3 * np.cos(angle.get_value()) * RIGHT + 3 * np.sin(angle.get_value()) * UP))

        horiz = DashedLine(10*LEFT + np.sin(angle.get_value()) * UP,
                           10*RIGHT + np.sin(angle.get_value()) * UP).add_updater(lambda m: m.put_start_and_end_on(10*LEFT + np.sin(angle.get_value()) * UP, 10*RIGHT + np.sin(angle.get_value()) * UP))

        vert = DashedLine(3*np.cos(angle.get_value()) * RIGHT + 10*UP,
                          3*np.cos(angle.get_value()) * RIGHT + 10*DOWN).add_updater(lambda m: m.put_start_and_end_on(3*np.cos(angle.get_value()) * RIGHT + 10*UP, 3*np.cos(angle.get_value()) * RIGHT + 10*DOWN))

        p3 = Dot(3 * np.cos(angle.get_value()) * RIGHT + np.sin(angle.get_value()) * UP).add_updater(lambda m: m.move_to(
            3 * np.cos(angle.get_value()) * RIGHT + np.sin(angle.get_value()) * UP))

        ellipse = ParametricFunction(lambda t: 3 * np.cos(t) * RIGHT + np.sin(t) * UP, t_range=[0, 0], color=RED).add_updater(
            lambda m: m.become(ParametricFunction(lambda t: 3 * np.cos(t) * RIGHT + np.sin(t) * UP, t_range=[0, angle.get_value()])))

        equation = MathTex(
            r"\frac{x^2}{3^2} + \frac{y^2}{1^2} = 1").scale(1.5).to_edge(UP + RIGHT)

        self.play(Create(plane))
        self.play(Create(c1))
        self.play(Create(c2))
        self.play(Create(rotor))
        self.play(Create(p1), Create(p2))
        self.play(Create(horiz), Create(vert))
        self.play(Create(p3))
        self.wait(1)
        self.play(angle.animate.set_value(0), rate_func=linear)
        self.add(ellipse)
        self.remove(p1, p2)
        self.wait(2)
        self.play(angle.animate.set_value(2*PI), rate_func=linear, run_time=12)
        self.wait(2)
        self.play(Uncreate(horiz), Uncreate(vert), Uncreate(
            p3), Uncreate(c1), Uncreate(c2), Uncreate(rotor))
        self.play(Write(equation))
        self.wait(1)
        self.play(Uncreate(ellipse), Unwrite(equation), Uncreate(plane))
        self.wait(2)
