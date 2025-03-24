from code.enemy import Enemy
from code.entity import Entity
from code.player import Player
from code.prize import Prize


class EntityMediator:
    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        if (ent1.rect.right >= ent2.rect.left and
                ent1.rect.left <= ent2.rect.right and
                ent1.rect.bottom >= ent2.rect.top and
                ent1.rect.top <= ent2.rect.bottom):
            if isinstance(ent1, Player) and isinstance(ent2, Enemy):
                ent1.health -= ent2.damage
                ent1.last_dmg = ent2.name
                ent2.health = 0
            elif isinstance(ent1, Enemy) and isinstance(ent2, Player):
                ent2.health -= ent1.damage
                ent2.last_dmg = ent1.name
                ent2.health = 0
            elif isinstance(ent1, Player) and isinstance(ent2, Prize):
                # ent1.score += ent2.score_value
                ent2.health = 0
            elif isinstance(ent1, Prize) and isinstance(ent2, Player):
                # ent2.score += ent1.score_value
                ent1.health = 0

    # @staticmethod
    # def __give_score(enemy: Enemy, entity_list: list[Entity]):
    #     if enemy.last_dmg == 'Player1':
    #         for ent in entity_list:
    #             if ent.name == 'Player1':
    #                 ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        entities_to_remove = []
        for ent in entity_list:
            if ent.health <= 0 and not isinstance(ent, Player):
                entities_to_remove.append(ent)
        for ent in entities_to_remove:
            entity_list.remove(ent)
    #
    # @staticmethod
    # def verify_health(entity_list: list[Entity]):
    #     for ent in entity_list:
    #         if ent.health <= 0:
    #             # if isinstance(ent, Enemy):
    #             #     EntityMediator.__give_score(ent, entity_list)
    #             entity_list.remove(ent)
