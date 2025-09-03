def test_formatpartition(storage_config,storage_client):
    partition = storage_config["server"]["device"] + "1"
    fstype = "ext4"
    out = storage_client.format_partition(partition,fstype)
    verify = storage_client.ssh.runcmd(f"sudo blkid {partition}")
    assert fstype in verify, f"Partition {partition} is not formatted with {fstype}. Output: {verify}"