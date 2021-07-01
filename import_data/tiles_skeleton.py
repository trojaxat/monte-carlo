import numpy as np
import cv2
import pandas as pd
import names
from supermarket import Supermarket
from customer import Customer


TILE_SIZE = 32

MARKET = """
##################
#b...........##
#b..##..##..##..##
#b..##..##..##..##
##..##..##..##..##
##..##..##..##..##
##..##..##..##..##
##...............#
##..C#..C#..C#...#
##..##..##..##...#
##...............#
##############GG##
""".strip()


class SupermarketMap:
    """Visualizes the supermarket background"""

    def __init__(self, layout, tiles):
        """
        layout : a string with each character representing a tile
        tiles   : a numpy array containing all the tile images
        """
        self.tiles = tiles
        # split the layout string into a two dimensional matrix
        self.contents = [list(row) for row in layout.split("\n")]
        self.ncols = len(self.contents[0])
        self.nrows = len(self.contents)
        self.image = np.zeros(
            (self.nrows*TILE_SIZE, self.ncols*TILE_SIZE, 3), dtype=np.uint8
        )
        self.prepare_map()

    def extract_tile(self, row, col):
        """extract a tile array from the tiles image"""
        y = row*TILE_SIZE
        x = col*TILE_SIZE
        return self.tiles[y:y+TILE_SIZE, x:x+TILE_SIZE]

    def get_tile(self, char):
        """returns the array for a given tile character"""
        if char == "#":
            return self.extract_tile(0, 0)
        elif char == "G":
            return self.extract_tile(7, 3)
        elif char == "C":
            return self.extract_tile(2, 8)
        elif char == "b":
            return self.extract_tile(0, 4)
        else:
            return self.extract_tile(1, 2)

    def prepare_map(self):
        """prepares the entire image as a big numpy array"""
        for row, line in enumerate(self.contents):
            for col, char in enumerate(line):
                bm = self.get_tile(char)
                y = row*TILE_SIZE
                x = col*TILE_SIZE
                self.image[y:y+TILE_SIZE, x:x+TILE_SIZE] = bm

    def draw(self, frame):
        """
        draws the image into a frame
        """
        frame[0:self.image.shape[0], 0:self.image.shape[1]] = self.image

    def write_image(self, filename):
        """writes the image into a file"""
        cv2.imwrite(filename, self.image)


if __name__ == "__main__":
    df = pd.read_csv(
        'import_data/data/monday_mc.csv', delimiter=',', parse_dates=True,  dtype=None)
    supermarket = Supermarket(df)
    cross = supermarket.generate_transition_probs()

    # each array spot is a customer, value is how many stops they make
    customerArray = [3, 4, 5, 2, 4]
    tiles = cv2.imread("import_data/media/tiles.png")

    # fix this!
    avatar = cv2.imread("import_data/media/sprite.jpeg")
    avatar = tiles[0*32+32, 4*32+32]
    market = SupermarketMap(MARKET, tiles)

    customers = []
    for customer_steps in customerArray:
        random_start = supermarket.random_first_state()
        new_customer = Customer(
            names.get_full_name(), cross, avatar, market, random_start)
        customers.append(new_customer)
    [(new_customer.next_state(), print(
        f"{new_customer.name} is in", new_customer.state)) for x in range(customer_steps)]

    background = np.zeros((500, 700, 3), np.uint8)
    tiles = cv2.imread("import_data/media/tiles.png")

    market = SupermarketMap(MARKET, tiles)

    while True:
        frame = background.copy()
        market.draw(frame)
        new_customer.draw(frame)
        # https://www.ascii-code.com/
        key = cv2.waitKey(1)

        if key == 113:  # 'q' key
            break

        cv2.imshow("frame", frame)

    cv2.destroyAllWindows()

    market.write_image("supermarket.png")
