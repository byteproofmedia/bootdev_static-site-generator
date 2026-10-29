from textnode import TextNode, TextType

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
