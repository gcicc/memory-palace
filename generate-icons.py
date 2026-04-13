#!/usr/bin/env python3
"""
Generate icons for Memory Palace PWA.
Creates 180px, 192px, and 512px PNGs with a brain/palace visual.
"""

from PIL import Image, ImageDraw, ImageFont
import os

def generate_icon(size):
    """Generate a single icon at the specified size."""

    # Create image with dark background
    img = Image.new('RGB', (size, size), color='#0d1117')
    draw = ImageDraw.Draw(img)

    # Draw background gradient effect (outer to inner)
    for i in range(size // 2):
        # Simple concentric circle darkening
        color_val = 13 + int((30 - 13) * (i / (size // 2)))
        draw.ellipse(
            [(size//2 - i, size//2 - i), (size//2 + i, size//2 + i)],
            outline=f'#{color_val:02x}{color_val + 7:02x}{color_val + 23:02x}'
        )

    # Draw stylized palace/brain structure
    # Central circular chamber (gold accent)
    margin = size // 6
    center = size // 2
    radius = (size - 2 * margin) // 3

    # Main palace dome
    draw.ellipse(
        [center - radius, center - radius - radius//2, center + radius, center + radius + radius//2],
        fill='#c4a882',
        outline='#c4a882'
    )

    # Left wing
    left_x = center - radius - radius // 2
    draw.ellipse(
        [left_x - radius//2, center - radius//3, left_x + radius//2, center + radius//3],
        fill='#b39872',
        outline='#c4a882'
    )

    # Right wing
    right_x = center + radius + radius // 2
    draw.ellipse(
        [right_x - radius//2, center - radius//3, right_x + radius//2, center + radius//3],
        fill='#b39872',
        outline='#c4a882'
    )

    # Top chamber
    draw.ellipse(
        [center - radius//2, center - radius - radius//2, center + radius//2, center - radius//4],
        fill='#a0886b',
        outline='#c4a882'
    )

    # Bottom chamber
    draw.ellipse(
        [center - radius//2, center + radius//4, center + radius//2, center + radius + radius//2],
        fill='#a0886b',
        outline='#c4a882'
    )

    # Add central accent point
    accent_r = radius // 4
    draw.ellipse(
        [center - accent_r, center - accent_r, center + accent_r, center + accent_r],
        fill='#0d1117',
        outline='#c4a882'
    )

    return img

def main():
    """Generate all icons."""
    script_dir = os.path.dirname(os.path.abspath(__file__))

    sizes = [180, 192, 512]

    for size in sizes:
        img = generate_icon(size)
        path = os.path.join(script_dir, f'icon-{size}.png')
        img.save(path, 'PNG')
        print(f'Generated {path}')

    print('\nAll icons generated successfully!')
    print('Ready to commit and deploy.')

if __name__ == '__main__':
    main()
