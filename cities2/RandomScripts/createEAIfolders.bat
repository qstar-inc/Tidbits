@echo off
set "baseFolder=%LocalAppData%Low\Colossal Order\Cities Skylines II\ModsData\ExtraAssetsImporter"

if not exist "%baseFolder%\CustomDecals" mkdir "%baseFolder%\CustomDecals"
if not exist "%baseFolder%\CustomDecals\Alphabet" mkdir "%baseFolder%\CustomDecals\Alphabet"
if not exist "%baseFolder%\CustomDecals\Beach" mkdir "%baseFolder%\CustomDecals\Beach"
if not exist "%baseFolder%\CustomDecals\Graffiti" mkdir "%baseFolder%\CustomDecals\Graffiti"
if not exist "%baseFolder%\CustomDecals\Ground" mkdir "%baseFolder%\CustomDecals\Ground"
if not exist "%baseFolder%\CustomDecals\Industry" mkdir "%baseFolder%\CustomDecals\Industry"
if not exist "%baseFolder%\CustomDecals\Leaf" mkdir "%baseFolder%\CustomDecals\Leaf"
if not exist "%baseFolder%\CustomDecals\Misc" mkdir "%baseFolder%\CustomDecals\Misc"
if not exist "%baseFolder%\CustomDecals\Numbers" mkdir "%baseFolder%\CustomDecals\Numbers"
if not exist "%baseFolder%\CustomDecals\Puddles" mkdir "%baseFolder%\CustomDecals\Puddles"
if not exist "%baseFolder%\CustomDecals\RoadAssets" mkdir "%baseFolder%\CustomDecals\RoadAssets"
if not exist "%baseFolder%\CustomDecals\RoadMarkings" mkdir "%baseFolder%\CustomDecals\RoadMarkings"
if not exist "%baseFolder%\CustomDecals\Stains" mkdir "%baseFolder%\CustomDecals\Stains"
if not exist "%baseFolder%\CustomDecals\Trash" mkdir "%baseFolder%\CustomDecals\Trash"
if not exist "%baseFolder%\CustomDecals\WallDecor" mkdir "%baseFolder%\CustomDecals\WallDecor"

if not exist "%baseFolder%\CustomSurfaces" mkdir "%baseFolder%\CustomSurfaces"
if not exist "%baseFolder%\CustomSurfaces\Brick" mkdir "%baseFolder%\CustomSurfaces\Brick"
if not exist "%baseFolder%\CustomSurfaces\Concrete" mkdir "%baseFolder%\CustomSurfaces\Concrete"
if not exist "%baseFolder%\CustomSurfaces\Grass" mkdir "%baseFolder%\CustomSurfaces\Grass"
if not exist "%baseFolder%\CustomSurfaces\Ground" mkdir "%baseFolder%\CustomSurfaces\Ground"
if not exist "%baseFolder%\CustomSurfaces\Misc" mkdir "%baseFolder%\CustomSurfaces\Misc"
if not exist "%baseFolder%\CustomSurfaces\Pavement" mkdir "%baseFolder%\CustomSurfaces\Pavement"
if not exist "%baseFolder%\CustomSurfaces\Rock" mkdir "%baseFolder%\CustomSurfaces\Rock"
if not exist "%baseFolder%\CustomSurfaces\Sand" mkdir "%baseFolder%\CustomSurfaces\Sand"
if not exist "%baseFolder%\CustomSurfaces\Tiles" mkdir "%baseFolder%\CustomSurfaces\Tiles"
if not exist "%baseFolder%\CustomSurfaces\Wood" mkdir "%baseFolder%\CustomSurfaces\Wood"

echo ExtraAssetsImporter folder structure created successfully.
echo %baseFolder%
pause