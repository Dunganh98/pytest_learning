import subprocess
import sys
from NLPLogic.simpleNLP import get_phrases


def test_wikiphrases_cli_with_argument():
    """Test calling wikiphrases.py as a CLI with an argument"""
    result = subprocess.run(
        [sys.executable, "wikiphrases.py", "Python (programming language)"],
        capture_output=True,
        text=True,
        check=True,
        timeout=10
    )
    assert result.returncode == 0
    assert "code readability" in result.stdout or "python" in result.stdout


def test_wikiphrases_cli_help():
    """Test calling wikiphrases.py with --help flag"""
    result = subprocess.run(
        [sys.executable, "wikiphrases.py", "--help"],
        capture_output=True,
        text=True,
        check=True,
        timeout=10
    )
    assert result.returncode == 0
    # Fire outputs help to stderr
    output = result.stdout + result.stderr
    assert "NAME" in output and "wikiphrases.py" in output


def test_wikiphrases_import():
    """Test that wikiphrases module can be imported and has correct structure"""
    import wikiphrases
    
    # Verify the module imports the required dependencies
    assert hasattr(wikiphrases, 'fire')
    assert hasattr(wikiphrases, 'get_phrases')
    
    # Verify get_phrases is callable
    assert callable(wikiphrases.get_phrases)


def test_get_phrases_integration():
    """Test the get_phrases function directly (integration test)"""
    phrases = get_phrases("Python (programming language)")
    assert phrases is not None
    assert isinstance(phrases, (list, tuple))
    assert len(phrases) > 0
