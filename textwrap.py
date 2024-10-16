#
# # wrap the string into a paragraph of given width
#
# import textwrap
#
# def wrap(string, max_width):
#
#     wrapper = textwrap.TextWrapper(width=max_width)
#     dedented_text = textwrap.dedent(text=string)
#     result = wrapper.fill(text=dedented_text)
#     return result
#
#
#     # i = 0
#     # j = max_width
#     # n = (len(string) // max_width) + (len(string) % max_width)
#     #
#     # for l in range(0, n - 1):
#     #     print(string[i:j:])
#     #     i = i + max_width
#     #     j = j + max_width
#
#     # return
#     # for i in range(0, len(string), max_width):
#     #     res = string[i:i+max_width]
#     #     if len(res) == max_width:
#     #         print(res)
#     #     else:
#     #         return res
#     # return textwrap.fill(string, max_width)
#     # return "\n".join([string[i:i + max_width] for i in range(0, len(string) - 1, max_width)])
#
# print(wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4))