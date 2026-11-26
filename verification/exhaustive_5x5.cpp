// Direct enumeration for the exceptional board, independent of verify.py.
// Compile with: c++ -std=c++17 -O3 exhaustive_5x5.cpp -o exhaustive_5x5
#include <array>
#include <cstdint>
#include <cstdio>

int main() {
    constexpr int side = 5;
    constexpr int cells = side * side;
    constexpr std::uint32_t patterns = 1u << cells;
    std::array<int, cells> right{}, down{};
    std::array<std::uint32_t, cells> neighbors{};
    for (int i = 0; i < side; ++i) {
        for (int j = 0; j < side; ++j) {
            int v = side * i + j;
            int up = side * ((i + side - 1) % side) + j;
            int left = side * i + (j + side - 1) % side;
            down[v] = side * ((i + 1) % side) + j;
            right[v] = side * i + (j + 1) % side;
            neighbors[v] = (1u << up) | (1u << down[v]) |
                           (1u << left) | (1u << right[v]);
        }
    }

    unsigned total_dominating = 0, horizontal = 0, valid = 0;
    for (std::uint32_t board = 0; board < patterns; ++board) {
        std::array<int, cells> count;
        bool dominated = true;
        for (int v = 0; v < cells; ++v) {
            count[v] = __builtin_popcount(board & neighbors[v]);
            if (count[v] == 0) {
                dominated = false;
                break;
            }
        }
        if (!dominated) continue;
        ++total_dominating;

        bool good_rows = true;
        for (int v = 0; v < cells; ++v) {
            if (count[v] == count[right[v]]) {
                good_rows = false;
                break;
            }
        }
        if (!good_rows) continue;
        ++horizontal;

        bool good_cols = true;
        for (int v = 0; v < cells; ++v) {
            if (count[v] == count[down[v]]) {
                good_cols = false;
                break;
            }
        }
        if (good_cols) ++valid;
    }
    std::printf("Boards: %u\nTotal dominating: %u\nAlso horizontal: %u\nFully valid: %u\n",
                patterns, total_dominating, horizontal, valid);
    return valid != 0;
}
