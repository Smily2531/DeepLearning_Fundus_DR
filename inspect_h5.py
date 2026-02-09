import h5py
import sys

H5_PATH = 'model/Updated-Xception-diabetic-retinopathy.h5'

try:
    f = h5py.File(H5_PATH, 'r')
except Exception as e:
    print('ERROR opening H5:', e)
    sys.exit(1)

print('Top-level keys:')
for k in f.keys():
    print(' -', k)

print('\nAttributes at root:')
for k, v in f.attrs.items():
    print(' -', k, ':', v)

if 'model_weights' in f:
    grp = f['model_weights']
    print('\nmodel_weights groups (layers):')
    for layer_name in grp.keys():
        print('\nLayer:', layer_name)
        layer_grp = grp[layer_name]
        for sub in layer_grp.keys():
            try:
                ds = layer_grp[sub]
                if hasattr(ds, 'shape'):
                    print('   ', sub, '->', getattr(ds, 'shape', None))
                else:
                    print('   ', sub)
            except Exception as e:
                print('   ', sub, ' (error)', e)
else:
    # inspect generic layout
    print('\nInspecting all datasets/groups:')
    def printer(name, obj):
        t = 'Group' if isinstance(obj, h5py.Group) else 'Dataset'
        shape = getattr(obj, 'shape', None)
        print(f"{t}: {name} shape={shape}")
    f.visititems(printer)

f.close()
