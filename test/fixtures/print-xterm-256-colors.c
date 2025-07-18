#include <stdio.h>

#define RESET_COLOR "\033[0m" // Resets color attributes to default

int main() {
    printf("256 Foreground Colors:\n");
    for (int i = 0; i <= 255; i++) {
        printf("\033[38;5;%dm%3d " RESET_COLOR, i, i); // Prints each color number in its respective foreground color, then resets to avoid bleeding
        if ((i + 1) % 16 == 0) { // New line every 16 colors for better readability
            printf("\n");
        }
    }
    printf("\n");

    printf("256 Background Colors:\n");
    for (int i = 0; i <= 255; i++) {
        printf("\033[48;5;%dm%3d " RESET_COLOR, i, i); // Prints each color number with its respective background color, then resets
        if ((i + 1) % 16 == 0) {
            printf("\n");
        }
    }
    printf("\n");

    return 0;
}
