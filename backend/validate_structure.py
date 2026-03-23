import os
import sys

print("Validating project structure...")

# Check critical paths
paths = [
    'tests',
    'tests/conftest.py',
    'tests/__init__.py',
    'app',
    'app/routes/error.py',
    'app/__init__.py',
    'app/routes/__init__.py'
]

base_path = os.path.dirname(os.path.abspath(__file__))
all_good = True

for path in paths:
    full_path = os.path.join(base_path, path)
    if not os.path.exists(full_path):
        print(f" Missing: {path}")
        all_good = False
    else:
        print(f" Found: {path}")

# Update PYTHONPATH for consistent imports
sys.path.insert(0, base_path)

try:
    from backend.tests.conftest import event_loop
    print(" Import test passed")
except ImportError as e:
    try:
        from tests.conftest import event_loop
        print(" Import test passed (relative import)")
    except ImportError as e:
        print(f" Import test failed: {e}")
        all_good = False

if all_good:
    print("\n All validations passed!")
else:
    print("\n Some validations failed")
    sys.exit(1)
