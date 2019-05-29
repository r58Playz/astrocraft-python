# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\toshi\\MicroHat\\applications\\games\\factories\\astrocraft-python'],
             binaries=[],
             datas=[("resources", "resources"), ("resources/avbin.dll", '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=["tcl", "tk"],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='AstroCraft',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='buildbeta')
