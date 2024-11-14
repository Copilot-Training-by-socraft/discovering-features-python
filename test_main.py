import main


def test_prints_hello_world(capsys):
    main.main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World"