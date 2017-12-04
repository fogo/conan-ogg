#include <ogg/ogg.h>
#include <iostream>
#include <stdlib.h>

int main(int argc, char** argv) {
    ogg_stream_state* stream = reinterpret_cast<ogg_stream_state*>(malloc(sizeof(ogg_stream_state)));
    int serialno = 0;
    while (ogg_stream_init(stream, serialno++) == -1) {}
    std::cout << "ogg stream created w/ serial number " << serialno << std::endl;
    ogg_stream_destroy(stream);
    std::cout << "ogg stream destroyed" << std::endl;

    return 0;
}
