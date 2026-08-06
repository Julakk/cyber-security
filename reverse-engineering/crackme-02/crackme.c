/*
 * Crackme #02 - Math Transform + Decoy
 * Compile: gcc -o crackme crackme.c
 *
 * Twist: ada decoy string ("DECOY_PASSWORD") yang keliatan kayak jawaban,
 * tapi itu cuma jebakan. Password asli dicek pakai transformasi matematika,
 * BUKAN string compare langsung.
 */
#include <stdio.h>
#include <string.h>

#define PASS_LEN 11
#define XOR_KEY2 0x42

// ⚠️ DECOY: ini SENGAJA ada supaya keliatan di 'strings', tapi ini BUKAN password asli.
// Kalau dicoba, fungsi check_decoy() akan selalu return "salah".
const char *DECOY_PASSWORD = "letmein123";

int check_decoy(const char *input) {
    // Fungsi ini sengaja selalu return 0 (gagal), meski input match DECOY_PASSWORD.
    // Ini jebakan buat orang yang cuma modal 'strings' doang tanpa baca logic beneran.
    if (strcmp(input, DECOY_PASSWORD) == 0) {
        return 0;  // <- tetap gagal walau "cocok"
    }
    return 0;
}

int check_real_password(const char *input) {
    if (strlen(input) != PASS_LEN) return 0;

    // Target = hasil transformasi (ord(c) * 3 + 7) % 256 dari password asli.
    unsigned char target[PASS_LEN] = {
        0xfd, 0xa0, 0x69, 0xa0, 0x5d, 0x60, 0xa0, 0x24, 0xee, 0xa0, 0x6a
    };

    for (int i = 0; i < PASS_LEN; i++) {
        unsigned char transformed = ((unsigned char)input[i] * 3 + 7) % 256;
        if (transformed != target[i]) {
            return 0;
        }
    }
    return 1;
}

int main() {
    unsigned char encoded_flag[] = {
        0x24, 0x2e, 0x23, 0x25, 0x39, 0x2f, 0x76, 0x36, 0x2a, 0x1d, 0x36,
        0x30, 0x76, 0x2c, 0x31, 0x24, 0x72, 0x30, 0x2f, 0x1d, 0x21, 0x2a,
        0x76, 0x2e, 0x2e, 0x71, 0x2c, 0x25, 0x71, 0x1d, 0x26, 0x72, 0x2c,
        0x71, 0x3f
    };
    int flag_len = sizeof(encoded_flag);

    char input[64];
    printf("=== Crackme #02: Math Transform + Decoy ===\n");
    printf("Masukkan password: ");

    if (fgets(input, sizeof(input), stdin) == NULL) {
        return 1;
    }
    input[strcspn(input, "\n")] = 0;

    // Cek decoy dulu (akan selalu gagal, ini bagian dari desain)
    if (check_decoy(input)) {
        printf("Ini seharusnya tidak pernah muncul.\n");
        return 1;
    }

    // Cek password asli lewat transformasi matematika
    if (check_real_password(input)) {
        printf("Password benar! Flag: ");
        for (int i = 0; i < flag_len; i++) {
            putchar(encoded_flag[i] ^ XOR_KEY2);
        }
        printf("\n");
    } else {
        printf("Password salah. Coba lagi!\n");
        return 1;
    }

    return 0;
}
