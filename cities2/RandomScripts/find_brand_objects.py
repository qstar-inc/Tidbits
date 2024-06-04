import os

objects = [
    "0003ddc9c81772841b87107ae9a88dad",
    "00f74c870f06a8746a426f97517e777b",
    "02c99a63f6fdd5e4993a7e48ca365ae7",
    "047a9f563c5146045bbdab53c207965d",
    "0a68b1f64c5842f4f9f116c5e94dd69e",
    "0c8a54d10924c4c4f967c512af8c74fe",
    "11325c4ff827a954380665d842c7b312",
    "135b0eb5d8b55e24b8cae28398b1ac00",
    "16888570e33f1ba4bb1f70d8a13236db",
    "1ba106031818e1946a3a0c50b2f482e2",
    "1d6fc888b7738bd4ea422c8a23ca6af5",
    "205f562936dc7194bab7cefe4b0f6f9a",
    "209315f1ccb86394fb19b5269db5859b",
    "3523125ac4634e1469b9fa77e0447e77",
    "37173135540498a4e8b7686dcaa92f2f",
    "381510ba31636e4418131f569495c09f",
    "384ed11a5eddc3a41bc90aebf10b43f2",
    "39295b9ca617cd54eae7f5c0d03bc9e7",
    "3da100ecfad738b42bb0970767ded006",
    "460bc75ecde76624db5d9c6c6d11d190",
    "4b7bccfb3e5a13140bace22571f5f877",
    "4f227c2a1c80f3348aa4136aa07680b2",
    "50af1995a9e4bfe43aadde3137cc6c8b",
    "54910a349e38b7c4384ae196a6c3670e",
    "592e71c02ef086149945afa28da64278",
    "5b346c7e24f8b9b45b66716acb792607",
    "5d6f2e1ce7a1a714f81943892b9da1c0",
    "603f63c276f0e874aa7f438c7740cd11",
    "655ebd65365a61f4b98e2f1a15944f54",
    "67e5463deb3db284aa1565843a50cee6",
    "6cdccc58a61c2314bb7e0b0781851485",
    "6e48309ea1b7a954c8baf5f1ea210df9",
    "71cbb886b233b3343bb41718cd90aa2e",
    "769b86b9cf728404692596b2fa353769",
    "785c3f4bfc5ec2f4f8383cc34073adc8",
    "7e2256e11e0adbc4fbb789f12c77e719",
    "810ef11cc80c00a44b9a7e31b3ec6960",
    "816cfd33a2a9d434284a650033f5245e",
    "8185f3c4cf05fbe478a55fb84487ec0c",
    "81a9639388eefdc4c9318b2c63180c6b",
    "83d0dd67f0bdd12439e0d00374e8b394",
    "855b25a090a4d7e4d98c9f278420dc70",
    "8741f473ee4efd94ea8051b27ab94158",
    "89621152bff79d944b9e228fc0ae57a6",
    "8a1d187a1a5510b408828e08d179a9cd",
    "91aa36263b51f2248a19de72eb0d7998",
    "941958e7a8d4e2b4490b1c461f25eede",
    "95fbcdf3298e3f649a274fd0cf3dc67e",
    "9cdb1284630869d4590b6173b8314b3e",
    "ae9b258671e05de4a896dc16452fdaf2",
    "b12031c2f9f2f9f40b5829c1859d1526",
    "b362f8de0471e6247ba6e3b782e42cea",
    "b3a0aa64736f28c45b16216e56c6dcd9",
    "b7f5ced0233fcb948a43883ebe08aa73",
    "b828678d6b5fa9546b37547b70cd3973",
    "bae8e8614aa23954dae6c55782cfff91",
    "bb82e6396dd235f428adb0be2c9e58b1",
    "bd5c6d42684f0604ab740e16bc28af47",
    "c2d0baae27f11d24fa776ada32407b0d",
    "c3de34db81c0c604bb27b090f04a062a",
    "cdd7ac5ceb8acdf4ca3ed817ca1da886",
    "d0a1c606b22c86543856f672819e20d1",
    "d2a3db2c3cbbc3741913503b586097f7",
    "d685afaba91b8514aaddff5008d7e725",
    "d6e1a56b4268294449b92beeb1cd6530",
    "d80b1360bce1579419c96bc8e0d67db3",
    "d947014c8239f144b8fe3aaa3c7002ec",
    "db3955b10e957054fa2691bd19017c97",
    "dbd8aa58534df3947a09bc7f3a1ac0dc",
    "dd965d822be18a94d92451755bf82042",
    "de07dd1ccd340784387f963fd47a9656",
    "df1ae4e2e01e3e244b6d4f1ec59626a3",
    "e0e96094bed98fa4fac05ee6ba447a00",
    "ed5bee5b4fd16874b84cc4b62a2e2d3e",
    "f6c94092fe9815846af6404a4d2edd0e",
    "fe03fdd49d2e2f34097f83d3dd63e5d1",
    "fe0ad3eac817c0c42bd9f48bc44e667d",
]
def search_text_in_prefab(directory, search_texts):
    counter = {}
    for folder_name, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.Prefab'):
                file_path = os.path.join(folder_name, file_name)
                with open(file_path, 'r') as file:
                    content = file.read()
                    for search_text in search_texts:
                        if search_text in content:
                            if search_text in counter:
                                counter.update({search_text : counter[search_text]+1})
                            else:
                                counter.update({search_text : 1})
                                
    print(len(counter))
    with open('find_brand_objects.txt', 'a') as file_to_write:
        dir = f'{directory.replace(os.getenv("LocalAppData")+"Low/Colossal Order/Cities Skylines II/.StreamingData~/Mixed Office/","")}'
        for key, item in counter.items():
            file_to_write.write(f'{key}\t{item}\t{dir}\n')
        file_to_write.write(f'-------------------------------------------\n')

directory_path = os.getenv('LocalAppData')+'Low/Colossal Order/Cities Skylines II/.StreamingData~/Mixed Office/'
with open('find_brand_objects.txt', 'w') as file_to_xwrite:
    file_to_xwrite.write("")
file_to_xwrite.close()
for folder_name, _, files in os.walk(directory_path):
    d = os.path.join(directory_path)
    if d.endswith("/") and os.path.dirname(folder_name) == d[:-1] and folder_name != directory_path:
        # print(folder_name)
        search_text_in_prefab(folder_name, objects)