from analyzer import analyze_log


def test_analyze_log_counts_levels(tmp_path):
    log_file = tmp_path / "test.log"
    log_file.write_text(
        "INFO Test message\n"
        "ERROR Something failed\n"
        "INFO Another message\n"
    )

    result = analyze_log(log_file)

    assert result["INFO"] == 2
    assert result["ERROR"] == 1
 