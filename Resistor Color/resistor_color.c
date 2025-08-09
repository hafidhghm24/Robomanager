#include "resistor_color.h"
#include <stdint.h>
uint16_t color_code(resistor_band_t code){
    return (uint16_t)code;
}

const resistor_band_t* colors(void){
    static const resistor_band_t colors[]={BLACK,
        BROWN,
        RED,
        ORANGE,
        YELLOW,
        GREEN,
        BLUE,
        VIOLET,
        GREY,
        WHITE};
    return colors;
}
