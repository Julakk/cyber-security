/*
 * Crackme #01 - Simple Serial Check
 * Compile: gcc -o crackme crackme.c
 *
 * Password yang benar akan decode dan print flag.
 * Flag disimpan ter-XOR di binary, bukan plaintext, supaya
 * `strings` doang gak cukup buat langsung dapetin flag.
 */
#include <stdio.h>
#include <string.h>

#define XOR_KEY 0x13
#define PASS_LEN 8

int main() {
    // Target = password_asli XOR 0x13, disimpan sebagai array byte.
    // Password aslinya TIDAK ada di sini dalam bentuk plaintext.
    unsigned char target[PASS_LEN] = {
        0x5b, 0x27, 0x70, 0x78, 0x20, 0x61, 0x32, 0x32
    };

    // Flag juga di-XOR pakai key yang sama, cuma di-decode kalau password benar.
    unsigned char encoded_flag[] = {
        0x75, 0x7f, 0x72, 0x74, 0x68, 0x61, 0x20, 0x65, 0x20, 0x61,
        0x60, 0x22, 0x7d, 0x74, 0x4c, 0x22, 0x60, 0x4c, 0x75, 0x66,
        0x7d, 0x4c, 0x21, 0x23, 0x21, 0x25, 0x6e
    };
    int flag_len = sizeof(encoded_flag);

    char input[64];
    printf("=== Crackme #01: Simple Serial Check ===\n");
    printf("Masukkan password: ");

    if (fgets(input, sizeof(input), stdin) == NULL) {
        return 1;
    }
    input[strcspn(input, "\n")] = 0;  // hapus newline

    if (strlen(input) != PASS_LEN) {
        printf("Password salah. (panjang tidak sesuai)\n");
        return 1;
    }

    int correct = 1;
    for (int i = 0; i < PASS_LEN; i++) {
        if (((unsigned char)input[i] ^ XOR_KEY) != target[i]) {
            correct = 0;
            break;
        }
    }

    if (correct) {
        printf("Password benar! Flag: ");
        for (int i = 0; i < flag_len; i++) {
            putchar(encoded_flag[i] ^ XOR_KEY);
        }
        printf("\n");
    } else {
        printf("Password salah. Coba lagi!\n");
        return 1;
    }

    return 0;
}
