guid = ["05ebbcb3-eca5-408e-98dd-685bbd6b0480",
        "10179648-10d6-4ffd-b164-cde9316ba3f0",
        "22194f84-9c6a-4571-a19a-a8b4f4b63344",
        "28fec9fe-a80d-40c6-bdcf-ebddb9536cdc",
        "4536a39c-2b13-43f3-88e8-810d3480c41e",
        "7e53a80d-53a3-4e63-a2e7-851cf6b62d2e",
        "7ffe6ccf-bf0d-440c-8ad7-5df0daa8381e",
        "82ae5d4d-337a-4e40-b5df-28c35d8df175",
        "9cd2872d-da2d-4869-9ee3-8bb12c574720",
        "a156f6cd-9908-4f4a-8ce0-d74d6e684a1c",
        "bd87bfae-5c86-4ff4-956c-99fad0526ec8",
        "f8f78a64-9d7d-4cbf-92e0-15ac344fdd1c",
]

# guid = ["12345678-abcd-efgh-ijkl-9876543210ab", "abcdefgh-ijkl-mnop-qrst-1234567890ab"]

for item in guid:
    reversed_guid = ''.join(part[::-1] for part in item.split('-'))
    print(reversed_guid)