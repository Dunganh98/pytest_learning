from NLPLogic.simpleNLP import search_wikipedia, summarize_wikipedia, get_text_blob, get_phrases
import pytest
from unittest.mock import patch
import wikipedia


def test_get_phrases():
    phrases = get_phrases("Python (programming language)")
    assert "code readability" in phrases
    assert "machine learning community" in phrases
    assert "python" in phrases

def test_search_wikipedia():
    result = search_wikipedia("Python")
    assert isinstance(result, list)
    assert "Python (programming language)" in result

def test_summarize_wikipedia():
    summary = summarize_wikipedia("Python (programming language)")
    assert "Python is a high-level, general-purpose programming language." in summary

def test_get_text_blob():
    text = "Python is a programming language."
    blob = get_text_blob(text)
    assert blob.correct() == text
    assert "python" in blob.noun_phrases


def test_search_wikipedia_disambiguation_error():
    """Test search_wikipedia handles DisambiguationError"""
    with patch('NLPLogic.simpleNLP.wikipedia.search') as mock_search:
        mock_search.side_effect = wikipedia.exceptions.DisambiguationError(
            'Test', ['Option1', 'Option2']
        )
        result = search_wikipedia("ambiguous")
        assert isinstance(result, str)
        assert "Disambiguation error" in result
        assert "Option1" in result or "Option2" in result


def test_search_wikipedia_page_error():
    """Test search_wikipedia handles PageError"""
    with patch('NLPLogic.simpleNLP.wikipedia.search') as mock_search:
        mock_search.side_effect = wikipedia.exceptions.PageError("Not found")
        result = search_wikipedia("nonexistent_page_xyz")
        assert isinstance(result, str)
        assert "Page not found" in result


def test_summarize_wikipedia_disambiguation_error():
    """Test summarize_wikipedia handles DisambiguationError"""
    with patch('NLPLogic.simpleNLP.wikipedia.summary') as mock_summary:
        mock_summary.side_effect = wikipedia.exceptions.DisambiguationError(
            'Test', ['Option1', 'Option2']
        )
        result = summarize_wikipedia("ambiguous")
        assert isinstance(result, str)
        assert "Disambiguation error" in result
        assert "Option1" in result or "Option2" in result


def test_summarize_wikipedia_page_error():
    """Test summarize_wikipedia handles PageError"""
    with patch('NLPLogic.simpleNLP.wikipedia.summary') as mock_summary:
        mock_summary.side_effect = wikipedia.exceptions.PageError("Not found")
        result = summarize_wikipedia("nonexistent_page_xyz")
        assert isinstance(result, str)
        assert "Page not found" in result