import numpy as np
from PIL import Image

# Define a simple 8x8 knight sprite using a color index
knight_sprite = np.array([
    [0, 0, 1, 1, 1, 0, 0, 0],  # Hood
    [0, 1, 1, 1, 1, 1, 7, 0],  # Hood and tip of Light Saber
    [1, 1, 2, 2, 2, 1, 7, 0],  # Forehead
    [1, 1, 3, 2, 3, 1, 7, 0],  # Eyes
    [1, 1, 4, 4, 4, 1, 7, 0],  # Beard
    [2, 1, 5, 1, 5, 1, 2, 0],  # Chest and Hands
    [0, 1, 6, 6, 6, 1, 8, 0],  # Belt and Hilt
    [0, 1, 5, 5, 5, 1, 0, 0],  # Bottom of robe
], dtype=np.uint8)

# Define a color palette (RGBA format)
palette = {
    0: (219, 98, 72), # Background
    1: (69, 43, 40), # Brown (Cloak and Shirt)
    2: (255, 222, 173), # Navajo White (Skin)
    3: (0, 0, 0), # Black (Eyes)
    4: (255, 255, 255), # White (Beard)
    5: (233, 223, 208), # Robe
    6: (139, 69, 19), # Saddle Brown (Belt)
    7: (102, 175, 238), # Light Blue (Light Saber)
    8: (105, 105, 105), # Dim Gray (Hilt)
}

# Create the image
img = Image.new("RGBA", (8, 8))
pixels = img.load()

# Apply colors from the sprite array
for y in range(8):
    for x in range(8):
        pixels[x, y] = palette[knight_sprite[y, x]]

# Save the sprite
img.save("knight_sprite_8x8.png")

# Show the sprite
img.show()
