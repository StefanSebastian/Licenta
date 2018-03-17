from utils import utils
from utils.tuples import Pixel
from color_analysis.detect.utils import calculate_pixel_probability


class AverageOnSuperpixelDetector:
    def __init__(self, model, window_size):
        self.model = model
        self.window_size = window_size
        self.pixel_probability_cache = {}

    def detect(self, image, superpixels, threshold):
        new_image = utils.generate_overlay_image(image)
        image = utils.convert_color(image, self.model.color_space)

        pos = 0
        for center in superpixels:  # iterate superpixels
            pos += 1
            utils.print_progress(pos, len(superpixels))

            superpixel = superpixels[center]
            total_prob = 0
            count = 0
            for pixel_pos in superpixel.get_pixels_pos(): # iterate all pixels in superpixel
                x_pixel, y_pixel = pixel_pos[0], pixel_pos[1]

                if self.window_size == 0:
                    prob = calculate_pixel_probability(image[x_pixel, y_pixel], self.model.components)
                else:
                    pixel = image[x_pixel, y_pixel]
                    p = Pixel(F1=pixel[0], F2=pixel[1], F3=pixel[2])
                    if p in self.pixel_probability_cache:
                        prob = self.pixel_probability_cache[p]
                    else:
                        prob = self.get_probability_with_neighbours(image[x_pixel, y_pixel])
                        self.pixel_probability_cache[p] = prob
                total_prob += prob
                count += 1

            # determine based on max probability if the region is classified as skin
            if (total_prob / count) > threshold:
                for pixel_pos in superpixel.get_pixels_pos():
                    x_pixel, y_pixel = pixel_pos[0], pixel_pos[1]
                    new_image[x_pixel, y_pixel] = [0, 0, 0]

        return new_image

    def get_probability_with_neighbours(self, pixel):
        max_prob = 0
        area = self.window_size
        for r_offset in range(-area, area, 1):
            for g_offset in range(-area, area, 1):
                for b_offset in range(-area, area, 1):
                    offset_pixel = [pixel[0] + r_offset, pixel[1] + g_offset, pixel[2] + b_offset]
                    prob = calculate_pixel_probability(offset_pixel, self.model.components)
                    if prob > max_prob:
                        max_prob = prob
        return max_prob
