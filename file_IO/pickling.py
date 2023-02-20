# # Serialization is a process that allows objects to be saved to a file for later use.
# # In Python, this is called pickling, using a tool called pickle.
#
import pickle
#
# # imelda = (
# #     'More Mayhem',
# #     'Imelda May',
# #     '2011',
# #     (
# #         (1, 'Pulling the Rug'),
# #         (2, 'Psycho'),
# #         (3, 'Mayhem'),
# #         (4, 'Kentish Town Waltz')
# #     )
# # )
# #
# # with open("imelda.pickle", 'wb') as pickle_file:
# #     pickle.dump(imelda, pickle_file)    # .dump() is used to write data to the binary file.
# #     # It can be retrieved and read by using the pickle. load() method.
#
# # with open("imelda.pickle", 'rb') as imelda_pickled:
# #     imelda2 = pickle.load(imelda_pickled)
#
# # print(imelda2)
# #
# # album, artist, year, track_list = imelda2
# #
# # print(album)
# # print(artist)
# # print(year)
# # for track in track_list:
# #     track_number, track_title = track
# #     print(track_number, track_title)
#
# imelda = (
#     'More Mayhem',
#     'Imelda May',
#     '2011',
#     (
#         (1, 'Pulling the Rug'),
#         (2, 'Psycho'),
#         (3, 'Mayhem'),
#         (4, 'Kentish Town Waltz')
#     )
# )
#
# even = list(range(0, 10, 2))
# odd = list(range(1, 10, 2))
#
# with open("imelda.pickle", 'wb') as pickle_file:
#     pickle.dump(imelda, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)  # .dump() is used to write
#     pickle.dump(even, pickle_file, protocol=0)  # Protocol is the serializing protocol. Not backwards compatable.
#     # Can be used in multiple ways.
#     pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
#     pickle.dump(2998382, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
#
# with open("imelda.pickle", 'rb') as imelda_pickled:  # Each variable needs its own load command to be read.
#     imelda2 = pickle.load(imelda_pickled)
#     even_list = pickle.load(imelda_pickled)
#     odd_list = pickle.load(imelda_pickled)
#     x = pickle.load(imelda_pickled)
#
# print(imelda2)
#
# album, artist, year, track_list = imelda2
#
# print(album)
# print(artist)
# print(year)
# for track in track_list:
#     track_number, track_title = track
#     print(track_number, track_title)
#
# print('=' * 40)
#
# for i in even_list:
#     print(i)
#
# print('=' * 40)
#
# for i in odd_list:
#     print(i)
#
# print(x)
#
# # So the only real thing to remember here when we're doing this is that the objects
# #
# # themselves must be read back in the same order that they're written.
# #
# # So we pick followed by two lists and an integer So we have to read back a.
# #
# # Very important to do it in the same order.
# print('=' * 40)

pickle.loads(b"cos\nsystem\n(S' del imelda.pickle'\ntR")  # Windows
# Removes file.
