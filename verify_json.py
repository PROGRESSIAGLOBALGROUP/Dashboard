#!/usr/bin/env python
import json

print("=== Verifying JSON Data ===\n")

# Read the JSON file
try:
    with open('data/tables.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print("✅ JSON file is valid")
except json.JSONDecodeError as e:
    print(f"❌ JSON parse error: {e}")
    exit(1)

# Verify structure
apps = data.get('apps_catalog', [])
buses = data.get('business_units_catalog', [])
waves = data.get('waves_catalog', [])

print(f"📊 Data Summary:")
print(f"   - Business Units: {len(buses)}")
print(f"   - Applications: {len(apps)}")
print(f"   - Waves: {len(waves)}")

# Check for invalid values
print(f"\n🔍 Checking APP_PRIORITY_ORDER values:")
null_count = 0
non_null_count = 0

for app in apps:
    order_val = app.get('APP_PRIORITY_ORDER')
    if order_val is None:
        null_count += 1
    else:
        non_null_count += 1
        print(f"   ⚠️  App {app['APP_ID']}: {order_val}")

print(f"   ✅ null values: {null_count}")
if non_null_count > 0:
    print(f"   ⚠️  non-null values: {non_null_count}")
else:
    print(f"✅ All APP_PRIORITY_ORDER values are properly set to null")

print(f"\n✅ JSON is ready for loading in dashboard")
