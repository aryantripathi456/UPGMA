def create_labels(start: str='A', end: str='C'):
    labels = [chr(i) for i in range(ord(start),ord(end)+1)]
    return labels
