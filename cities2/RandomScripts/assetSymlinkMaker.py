import os
from pathlib import Path

def create_required_folder_structure():
    base_path = Path(os.getenv('LOCALAPPDATA'), '..', 'LocalLow', 'Colossal Order', 'Cities Skylines II', 'ModsData', 'StarQ Asset Patch')
    if not base_path.exists():
        base_path.mkdir(parents=True, exist_ok=True)
    return base_path

def find_assets_and_dlls(base_cache_path):
    assets_and_dlls = []
    for root, dirs, files in os.walk(base_cache_path):
        asset_dirs = [d for d in dirs if d.lower().startswith('assets')]
        if asset_dirs and any(file.endswith('.dll') for file in files):
            dll_file = next(file for file in files if file.endswith('.dll'))
            for asset_dir in asset_dirs:
                if not "CompanyModParadoxInteractive" in dll_file:
                    assets_and_dlls.append((Path(root, asset_dir), Path(root, dll_file)))
    return assets_and_dlls

def clear_existing_symlinks(target_dir):
    for item in target_dir.iterdir():
        if item.is_symlink():
            item.unlink()
            print(f'Removed existing symlink: {item}')

def create_symlinks(assets_and_dlls, target_dir):
    for assets_path, dll_path in assets_and_dlls:
        dll_name = dll_path.stem
        asset_index = assets_path.name[6:].replace('-', '').replace('_', '')
        link_name = f"{dll_name}_{asset_index}" if asset_index else dll_name
        symlink_path = target_dir / link_name
        try:
            if symlink_path.exists() or symlink_path.is_symlink():
                if symlink_path.is_symlink() or symlink_path.is_dir():
                    symlink_path.unlink()
                else:
                    print(f"Cannot create symlink, a file with the same name exists: {symlink_path}")
                    continue
            os.symlink(assets_path, symlink_path)
            # print(f'Symlink created: {symlink_path} -> {assets_path}')
        except OSError as e:
            print(f'Failed to create symlink for {dll_path}: {e}')

def main():
    target_dir = create_required_folder_structure()
    base_cache_path = Path(os.getenv('LOCALAPPDATA'), '..', 'LocalLow',  'Colossal Order', 'Cities Skylines II', '.cache', 'Mods', 'mods_subscribed')
    
    if not base_cache_path.exists():
        print(f"Base cache path does not exist: {base_cache_path}")
        return

    assets_and_dlls = find_assets_and_dlls(base_cache_path)
    if not assets_and_dlls:
        print("No assets and DLL files found.")
        return

    clear_existing_symlinks(target_dir)
    create_symlinks(assets_and_dlls, target_dir)

if __name__ == '__main__':
    main()
