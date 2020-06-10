import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)





class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()
    
    def get_friends(self, user_id):
        return self.friendships[user_id]

    def bft(self, user_id):
        #uses a queue
        start = user_id
        q = Queue()
        q.enqueue([user_id])

        visited = set()
        # visited.add(start)
        current = None
        counter = 0
        while q.size() > 0:
            #deq current
            current = q.dequeue()
            if counter < 1:
                print('counter', counter)
                if current[-1] == start and len(current) > 1:
                    counter+=1
                #add current vertex to visited if it isn't already there
                if current[-1] not in visited:
                    print('current friend', current[-1])
                    print('current', current)
                    visited.add(current[-1])

                    #add all neighbors to q
                    for vert in self.get_friends(current[-1]):
                        new_path = [*current, vert]
                        q.enqueue(new_path)
        return current



    def populate_graph(self, num_users, avg_friendships):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i}")
        # Create Frienships
        # Generate all possible friendship combinations
        possible_friendships = []

        # Avoid duplicates by ensuring the first number is smaller than the second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
                
            # Shuffle the possible friendships
            random.shuffle(possible_friendships)
        # Create friendships for the first X pairs of the list
        # X is determined by the formula: num_users * avg_friendships // 2
        # Need to divide by 2 since each add_friendship() creates 2 friendships


        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
        
            


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        #each key is a friend and each value is the path to that friend

        friendships = self.friendships[user_id]
        # print('friendships', friendships)

        for friend in friendships:
            print('friend', friend)
            # print(self.bft(friend))
            path = self.bft(friend)
        #     print('path', path)
            if user_id not in path:
                print('path in the if', path)
                visited[path[-1]] = path



        print('visited', visited)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    print(sg.populate_graph(10, 2))
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    # print(connections)
