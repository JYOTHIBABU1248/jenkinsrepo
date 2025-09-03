def test_create_partition(storage_config, storage_client):
    device = storage_config["server"]["device"]
    storage_client.create_partition(device)

    # Verify partition exists using lsblk
    verify = storage_client.ssh.runcmd(f"lsblk -o NAME,SIZE,TYPE {device}")
    print("\nPartition table:\n", verify)

    assert "part" in verify, f"No partition created on {device}"
