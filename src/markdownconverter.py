import re

from textnode import TextNode, TextType

def text_to_textnodes(text) -> list[TextNode]:
    nodes: list[TextNode] = [TextNode(text, TextType.TEXT)]
    #bold nodes
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    #italic nodes
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    #code nodes
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    #link nodes
    nodes = split_nodes_link(nodes)
    #image nodes
    nodes = split_nodes_image(nodes)

    return nodes

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text_list = node.text.split(delimiter)
        split_nodes: list[TextNode] = []
        if len(text_list) % 2 == 0:
            raise Exception(f"Error: Invalid Markdown syntax, no closing delimeter \"{delimiter}\"")
        for i in range(len(text_list)):
            if text_list[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(text_list[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(text_list[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    print(f"Running split_nodes_image:\n{old_nodes}")
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        original_text = node.text
        remaining_text = original_text
        images = extract_markdown_images(original_text)
        if images:
            for image in images:
                image_alt = image[0]
                image_link = image[1]
                #split original string by this image node
                sections = remaining_text.split(f"![{image_alt}]({image_link})", 1)
                if len(sections) >= 1 and sections[0] != '':
                    print(f"Adding to new_nodes: {TextNode(sections[0], TextType.TEXT)}")
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                if len(sections) >=2:
                    remaining_text = sections[1]
                else:
                    remaining_text = ''
                print(f"Adding to new_nodes: {TextNode(image_alt, TextType.IMAGE, image_link)}")
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
                print(f"Remaining text: {remaining_text}")
                continue
            if remaining_text != '':
                print(f"Adding to new_nodes: {TextNode(remaining_text, TextType.TEXT)}")
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
            continue
        new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    print(f"Running split_nodes_link:\n{old_nodes}")
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        original_text = node.text
        remaining_text = original_text
        links = extract_markdown_links(original_text)
        if links:
            for link in links:
                link_text = link[0]
                link_link = link[1]
                #split original string by this image node
                sections = remaining_text.split(f"[{link_text}]({link_link})", 1)
                if len(sections) >= 1 and sections[0] != '':
                    print(f"Adding to new_nodes: {TextNode(sections[0], TextType.TEXT)}")
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                if len(sections) >= 2:
                    remaining_text = sections[1]
                else:
                    remaining_text = ''
                print(f"Adding to new_nodes: {TextNode(link_text, TextType.LINK, link_link)}")
                new_nodes.append(TextNode(link_text, TextType.LINK, link_link))
                continue
            if remaining_text != '':
                print(f"Adding to new_nodes: {TextNode(remaining_text, TextType.TEXT)}")
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
            continue
        new_nodes.append(node)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
