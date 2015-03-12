# WAMSAGE - West and Moon's Super Awesome Game Engine - entity classes

import collections.abc
import logging

class Entity:
    def __init__(self, name, description, container):
        super().__init__()
        self.name = name
        self.description = description
        self.container = container
        self._logger = logging.getLogger('entity')

class Container(Entity, collections.abc.Sized, collections.abc.Iterable, collections.abc.Container):
    def __init__(self, name, description, container, contents):
        super().__init__(name, description, container)
        self._contents = set(contents)

    def __len__(self):
        return len(self._contents)

    def __iter__(self):
        return iter(self._contents)

    def __contains__(self, entity):
        return entity in self._contents

    def add(self, entity, move=True):
        if move:
            entity.container.discard(entity)
            entity.container = self
        self._contents.add(entity)
        self._logger.debug('added entity %s to container %s', entity.name, self.name)

    def remove(self, entity):
        try:
            self._contents.remove(entity)
        except KeyError:
            self._logger.debug(
                'entity %s not in container %s, so not removed',
                entity.name, self.name)
            raise
        else:
            self._logger.debug(
                'entity %s removed from container %s',
                entity.name, self.name)

    def discard(self, entity):
        try:
            self.remove(entity)
        except KeyError:
            pass
