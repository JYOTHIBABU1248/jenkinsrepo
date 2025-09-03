import json
import pytest

def test_fio(storage_config, storage_client):
    mount_point = storage_config["server"]["mount_point"]
    output = storage_client.run_fio(mount_point, runtime=60)
    print("outputtttt",output)
    try:
        fio_result = json.loads(output)
    except json.JSONDecodeError:
        pytest.fail(f"Failed to parse fio output:\n{output}")

    read_iops = fio_result["jobs"][0]["read"]["iops"]
    write_iops = fio_result["jobs"][0]["write"]["iops"]

    print(f"\nFIO Results: Read IOPS={read_iops}, Write IOPS={write_iops}")

    # Basic validation: ensure some I/O happened
    assert read_iops > 0, "No read operations recorded by fio"
    assert write_iops > 0, "No write operations recorded by fio"
