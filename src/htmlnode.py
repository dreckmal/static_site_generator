

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        return "".join(' {0}="{1}"'.format(k, v) for k, v in self.props.items())

    def __repr__(self):
        return f"(HTMLNode({self.tag}, {self.value}, {self.children}, {self.props}))"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode must have a tag")
        if self.children == None:
            raise ValueError("ParentNode must have children")
        if self.children == []:
            raise ValueError("ParentNode cannot be empty")
        if self.value != None:
            raise ValueError("ParentNode cannot have a value")
        parent_str = self.props_to_html() or ""
        child_str = "".join([child.to_html() for child in self.children])
        return f"<{self.tag}{parent_str}>{child_str}</{self.tag}>"



class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode must have a value")
        if self.tag == None:
            return self.value
        props_str = self.props_to_html() if self.props else ""
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"


#class Hero:
#    def __init__(self, name, health):
#        self.name = name
#        self.health = health
#
#class Warrior(Hero):
#    def __init__(self, name, health, strength):
#        super().__init__(name, health)
#        self.strength = strength
#
#class Archer(Hero):
#    def __init__(self, name, health, arrows):
#        super().__init__(name, health)
#        self._arrows = arrows
#
#    def shoot(self, target):
#        if self._arrows <= 0:
#            raise Exception("Not enough arrows")
#        self._arrows -= 1
#        target.health -= 10
######
