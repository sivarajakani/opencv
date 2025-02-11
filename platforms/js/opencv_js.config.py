# Classes and methods whitelist

core = {
    '': []
}

imgproc = {
    '': [
        'resize',
    ]
}
white_list = makeWhiteList([core, imgproc])

# namespace_prefix_override['dnn'] = ''  # compatibility stuff (enabled by default)
# namespace_prefix_override['aruco'] = ''  # compatibility stuff (enabled by default)
