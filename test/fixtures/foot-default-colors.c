#include <stdbool.h>
#include <stdio.h>
#include <stdint.h>

// From dnkl/foot config.c:
// https://codeberg.org/dnkl/foot/src/commit/692b22cbbb24efa91cb24446d189bc8c2535c1ac/config.c#L38-L107

#define cube6(r, g) \
    r|g|0x00, r|g|0x5f, r|g|0x87, r|g|0xaf, r|g|0xd7, r|g|0xff

#define cube36(r) \
    cube6(r, 0x0000), \
    cube6(r, 0x5f00), \
    cube6(r, 0x8700), \
    cube6(r, 0xaf00), \
    cube6(r, 0xd700), \
    cube6(r, 0xff00)

static const uint32_t default_color_table[256] = {
    // Regular
    0x242424,
    0xf62b5a,
    0x47b413,
    0xe3c401,
    0x24acd4,
    0xf2affd,
    0x13c299,
    0xe6e6e6,

    // Bright
    0x616161,
    0xff4d51,
    0x35d450,
    0xe9e836,
    0x5dc5f8,
    0xfeabf2,
    0x24dfc4,
    0xffffff,

    // 6x6x6 RGB cube
    // (color channels = i ? i*40+55 : 0, where i = 0..5)
    cube36(0x000000),
    cube36(0x5f0000),
    cube36(0x870000),
    cube36(0xaf0000),
    cube36(0xd70000),
    cube36(0xff0000),

    // 24 shades of gray
    // (color channels = i*10+8, where i = 0..23)
    0x080808, 0x121212, 0x1c1c1c, 0x262626,
    0x303030, 0x3a3a3a, 0x444444, 0x4e4e4e,
    0x585858, 0x626262, 0x6c6c6c, 0x767676,
    0x808080, 0x8a8a8a, 0x949494, 0x9e9e9e,
    0xa8a8a8, 0xb2b2b2, 0xbcbcbc, 0xc6c6c6,
    0xd0d0d0, 0xdadada, 0xe4e4e4, 0xeeeeee
};

/*
 * Color Functions
 *
 * Hex color values from default_color_table only valid if the user has not
 * changed theme away from the default.
 *
*/

// Function to set foreground color using an integer code
void set_foreground_color(int color_code) {
    printf("\x1b[38;5;%dm", color_code);
}

// Function to set background color using an integer code
void set_background_color(int color_code) {
    printf("\x1b[48;5;%dm", color_code);
}

// Function to reset colors
void reset_colors() {
    printf("\x1b[0m");
}

int main(void) {
  size_t total_size = sizeof(default_color_table);
  size_t element_size = sizeof(default_color_table[0]);
  size_t array_length = total_size / element_size;

  bool print_heading = true;

  // bold heading underlined - fg & bg demo in green
  static char boldU[] = "\x1b[1;4;m\0";
  static char cynfg[] = "\x1b[1;4;37m\0";
  static char grnfg[] = "\x1b[1;4;51;32m\0";
  static char grnbg[] = "\x1b[1;4;52;42m\0";
  static char blkfg[] = "\x1b[1;4;30m\0";
  static char reset[] = "\x1b[0m\0";
  if (print_heading == 1)
    printf("%s%scolor   num %sfg %s%sbg%s\n", boldU, cynfg, grnfg, blkfg, grnbg, reset);
  // Prints lines: #xxxxxx nn █ <- color block
  for (int i=0; i < array_length; i++) {
    printf("#%06llx %03i", default_color_table[i], i);
    printf(" ");
    set_foreground_color(i);
    printf("█"); // fg color block (utf-8 full block char '█')
    reset_colors();
    printf("  "); // space
    set_background_color(i);
    printf(" "); // bg color block (single space ' ')
    reset_colors();
    printf("\n");
  }
  return 0;
}
