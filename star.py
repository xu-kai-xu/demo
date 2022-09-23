import sqlite3

class Star:
    db = r'./stars.db'

    def __init__(self, name):
        self.name = name
        self.not_found = False
        if not self._lookup_en() and not self._lookup_cn():
            self.not_found = True

    def _lookup(self, colname):
        try:
            conn = sqlite3.connect(self.db)
            cur = conn.cursor()
            sql = f'SELECT stars.name_en, stars.name_cn, stars.brightness, cons.name, cons.name_cn FROM stars LEFT JOIN cons ON cons.abbr_iau = stars.cons_abbr WHERE stars.{colname} LIKE ? ORDER BY stars.top20 DESC, stars.commonly_used DESC, stars.brightness'
            cur.execute(sql, ('%' + self.name + '%',))
            result = cur.fetchone()
            if result:
                self.name_en, self.name_cn, self.brightness, self.cons_name, self.cons_name_cn = result
                return True
            else:
                return False
        finally:
            conn.close()

    def _lookup_en(self):
        return self._lookup('name_en')

    def _lookup_cn(self):
        return self._lookup('name_cn')

    def __str__(self):
        if self.not_found:
            return f'{self.name}: not found.'

        return f'{self.name} in {self.cons_name}: {self.cons_name_cn} 的 {self.name_cn}, 视星等 {self.brightness}.'

    __repr__ = __str__

if __name__ == '__main__':
    print(Star('Vega'))
    print(Star('织女一'))
    print(Star('織女一'))  # 简繁转换没有做