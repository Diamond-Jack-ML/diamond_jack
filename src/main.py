# src/main.py or wherever you need to use the Confluence services
from services.confluence_service import create_confluence_page

# Example usage
space_key = 'MVP'
parent_page_id = '14778582'
page_title = 'Onboarding Checklist for New Sales Representative'
content_body = """
<h2>Test Page with Various UI Elements</h2>

<h3>Pre-Start Preparation</h3>

<p><strong><u>To Do:</u></strong></p>
<p>List out key milestones and their deadlines.</p>
<h3><strong><u>Milestones:</u></strong></h3>
<ul>
<li>
<p>Define services (6/12/24)</p></li>
<li>
<p>Develop sales script (6/13/24)</p></li>
<li>
<p>Create landing page (6/14/24)</p></li></ul>
<p><time datetime="2024-06-21" /> </p>
<p />
"""


create_confluence_page(space_key, parent_page_id, page_title, content_body)
