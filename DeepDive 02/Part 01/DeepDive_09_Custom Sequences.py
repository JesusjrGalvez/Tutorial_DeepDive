

class Polygon:
    def __init__(self, *pts):
        if pts:
            self._pts = [Point(*pt) for pt in pts]
        else:
            self._pts = []

    def __repr__(self):
        pts_str = ', '.join([str(pt) for pt in self._pts])
        return f'Polygon({pts_str})'

    def __len__(self):
        return len(self._pts)

    def __getitem__(self, s):
        return self._pts[s]

    def __setitem__(self, s, value):
        # we first should see if we have a single Point
        # or an iterable of Points in value
        try:
            rhs = [Point(*pt) for pt in value]
            is_single = False
        except TypeError:
            # not a valid iterable of Points
            # maybe a single Point?
            try:
                rhs = Point(*value)
                is_single = True
            except TypeError:
                # still no go
                raise TypeError('Invalid Point or iterable of Points')

        # reached here, so rhs is either an iterable of Points, or a Point
        # we want to make sure we are assigning to a slice only if we
        # have an iterable of points, and assigning to an index if we
        # have a single Point only
        if (isinstance(s, int) and is_single) \
                or isinstance(s, slice) and not is_single:
            self._pts[s] = rhs
        else:
            raise TypeError('Incompatible index/slice assignment')

    def __add__(self, pt):
        if isinstance(pt, Polygon):
            new_pts = self._pts + pt._pts
            return Polygon(*new_pts)
        else:
            raise TypeError('can only concatenate with another Polygon')

    def append(self, pt):
        self._pts.append(Point(*pt))

    def extend(self, pts):
        if isinstance(pts, Polygon):
            self._pts = self._pts + pts._pts
        else:
            # assume we are being passed an iterable containing Points
            # or something compatible with Points
            points = [Point(*pt) for pt in pts]
            self._pts = self._pts + points

    def __iadd__(self, pts):
        self.extend(pts)
        return self

    def insert(self, i, pt):
        self._pts.insert(i, Point(*pt))

    def __delitem__(self, s):
        del self._pts[s]

    def pop(self, i):
        return self._pts.pop(i)