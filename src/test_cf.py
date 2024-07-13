import unittest
import os
import shutil
from unittest.mock import patch, Mock
from src.services.confluence_getters import get_spaces, get_pages_in_space, get_page_content, save_to_text_file, process_confluence_space, fetch_and_store_confluence_data, load_text_files

class TestConfluenceGetters(unittest.TestCase):

    @patch('src.services.confluence_getters.requests.get')
    def test_get_spaces(self, mock_get):
        mock_response = Mock()
        expected_output = {'results': [{'key': 'SPACE1'}, {'key': 'SPACE2'}]}
        mock_response.json.return_value = expected_output
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response
        
        result = get_spaces()
        self.assertEqual(result, expected_output['results'])

    @patch('src.services.confluence_getters.requests.get')
    def test_get_pages_in_space(self, mock_get):
        mock_response = Mock()
        expected_output = {'page': {'results': [{'id': '123'}, {'id': '456'}]}}
        mock_response.json.return_value = expected_output
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response
        
        result = get_pages_in_space('SPACE1')
        self.assertEqual(result, expected_output['page']['results'])

    @patch('src.services.confluence_getters.requests.get')
    def test_get_page_content(self, mock_get):
        mock_response = Mock()
        expected_output = {'body': {'storage': {'value': '<p>Content</p>'}}}
        mock_response.json.return_value = expected_output
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response
        
        result = get_page_content('123')
        self.assertEqual(result, expected_output['body']['storage']['value'])

    def test_save_to_text_file(self):
        content = "Sample content"
        filename = "test_output/test_file.txt"
        
        save_to_text_file(content, filename)
        
        with open(filename, 'r', encoding='utf-8') as f:
            result = f.read()
        self.assertEqual(result, content)

    @patch('src.services.confluence_getters.get_pages_in_space')
    @patch('src.services.confluence_getters.get_page_content')
    @patch('src.services.confluence_getters.save_to_text_file')
    def test_process_confluence_space(self, mock_save, mock_get_content, mock_get_pages):
        mock_get_pages.return_value = [{'id': '123', 'title': 'Test Page'}]
        mock_get_content.return_value = 'Page Content'
        
        process_confluence_space('SPACE1', 'test_output')
        
        mock_save.assert_called_once_with('Page Content', 'test_output/Test Page.txt')

    @patch('src.services.confluence_getters.get_spaces')
    @patch('src.services.confluence_getters.process_confluence_space')
    def test_fetch_and_store_confluence_data(self, mock_process, mock_get_spaces):
        mock_get_spaces.return_value = [{'key': 'SPACE1', 'name': 'Space One'}]
        
        fetch_and_store_confluence_data('test_output')
        
        mock_process.assert_called_once_with('SPACE1', 'test_output/Space One')

    def test_load_text_files(self):
        # Clean up any existing test output directory
        shutil.rmtree('test_output', ignore_errors=True)

        # Prepare test data
        os.makedirs('test_output', exist_ok=True)
        filenames = ['test_output/file1.txt', 'test_output/file2.txt']
        contents = ["Content of file 1", "Content of file 2"]
        for filename, content in zip(filenames, contents):
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
        
        result = load_text_files('test_output')
        self.assertEqual(result, contents)

    def tearDown(self):
        # Clean up after each test
        shutil.rmtree('test_output', ignore_errors=True)

if __name__ == '__main__':
    unittest.main()
