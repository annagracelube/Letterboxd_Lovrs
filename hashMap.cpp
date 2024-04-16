#include "hashMap.h"

int hashMap::hash(std::string &key)
{
    return key.length() % capacity;
}

bool hashMap::search(std::string key)
{
    int bucketIndex = hash(key);
    for(auto element:map[bucketIndex])
    {
        if(element.first == key)
        {
            return true;
        }
    }
    return false;
}

void hashMap::insert(std::string key, std::vector<std::string> values)
{
    if(size >= capacity * 0.75)
    {
        resizeAndRehash(capacity * 2);
    }
    int bucketIndex = hash(key);
    if(search(key))
    {
        return;
    }
    std::pair<std::string, std::vector<std::string>> pair(key, values);
    map[bucketIndex].push_back(pair);
    size++;
}

void hashMap::resizeAndRehash(int newCapacity)
{
    std::vector<std::vector<std::pair<std::string, std::vector<std::string>>>> newMap(newCapacity);
    for(auto bucket:map)
    {
        for(auto key:bucket)
        {
            int newBucketIndex = hash(key.first);
            std::pair<std::string, std::vector<std::string>> pair(key.first, key.second);
            newMap[newBucketIndex].push_back(pair);
        }
    }
    map = newMap;
    capacity = newCapacity;
}

void hashMap::printOut()
{
    for(auto bucket:map)
    {
        for(auto key:bucket)
        {
            std::cout << key.first << " ";
            for(auto it:key.second)
            {
                std::cout << it << " ";
            }
            std::cout << "\n";
        }
    }
}
