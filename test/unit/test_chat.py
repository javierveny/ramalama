import pytest
from unittest.mock import MagicMock
from ramalama.chat import RamaLamaShell

def test_input_with_backslash():
    # fake arguments to not get errors
    mock_args = MagicMock()
    mock_args.prefix = "> "
    mock_args.url = "http://localhost:8080"
    mock_args.model = "test-model"
    mock_args.rag = None
    mock_args.mcp = []
    mock_args.summarize_after = 0
    mock_args.color = "never"
    
    # instance of RamaLamaShell with the fake args
    ramalama = RamaLamaShell(mock_args)
    
    # disable network function
    ramalama._req = MagicMock(return_value="Answer")
    
    # Case 1, with backslash
    assert ramalama.default("Hola\\") is False
    assert ramalama.content == ["Hola"]
    

def test_input_continuation_with_backslash():
    # fake arguments to not get errors
    mock_args = MagicMock()
    mock_args.prefix = "> "
    mock_args.url = "http://localhost:8080"
    mock_args.model = "test-model"
    mock_args.rag = None
    mock_args.mcp = []
    mock_args.summarize_after = 0
    mock_args.color = "never"

    # instance of RamaLamaShell with the fake args
    ramalama = RamaLamaShell(mock_args)
    ramalama._req = MagicMock(return_value="Answer") # disable network function

    # case 2, we add text after backslash
    assert ramalama.default("Hola \\") is False
    assert ramalama.content == ["Hola "]

    # we add text after
    assert ramalama.default("Mundo") is not False
    assert ramalama.content == []

def test_input_without_backslash():
    # fake arguments to not get errors
    mock_args = MagicMock()
    mock_args.prefix = "> "
    mock_args.url = "http://localhost:8080"
    mock_args.model = "test-model"
    mock_args.rag = None
    mock_args.mcp = []
    mock_args.summarize_after = 0
    mock_args.color = "never"

    # instance of RamaLamaShell with the fake args
    ramalama = RamaLamaShell(mock_args)
    ramalama._req = MagicMock(return_value="Answer") # disable network function
    
    # case 3, no backslash
    result = ramalama.default("Hola")
    assert result is not False # it does not return True
    assert ramalama.content == [] # the message has been sended