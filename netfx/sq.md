sequenceDiagram
    autonumber
    actor User as Пользователь (Браузер)
    participant FE as Frontend (React + hls.js)
    participant GW as API Gateway
    participant MS as Media Service
    participant DB as База данных (PostgreSQL/Redis)
    participant CDN as CDN / S3 Storage

    Note over User, CDN: Этап 1: Инициация просмотра
    User->>FE: Нажимает кнопку "Смотреть" для фильма ID=123
    FE->>GW: GET /api/v1/movies/123/stream <br/>(Headers: Authorization: Bearer <JWT>)
    
    Note over GW, MS: Этап 2: Аутентификация и Авторизация
    GW->>GW: Проверка валидности JWT токена
    GW->>MS: Перенаправление запроса в Media Service
    
    MS->>DB: Проверка статуса подписки и прав пользователя <br/>(SELECT * FROM subscriptions WHERE user_id = ?)
    DB-->>MS: Подписка активна (или кэш Redis)
    
    Note over MS, CDN: Этап 3: Генерация защищенной ссылки
    MS->>CDN: Запрос на генерацию Signed URL (временной ссылки) <br/>для манифеста .m3u8 (HLS)
    CDN-->>MS: Возвращает Signed URL (действует, например, 1 час)
    
    MS-->>GW: 200 OK { "streamUrl": "https://cdn.../movie123.m3u8?signature=..." }
    GW-->>FE: Передача ответа с streamUrl
    
    Note over User, CDN: Этап 4: Непосредственный стриминг (без участия бэкенда)
    FE->>FE: Инициализация видеоплеера (hls.js) с полученным streamUrl
    FE->>CDN: GET запрос на загрузку манифеста .m3u8
    CDN-->>FE: Возврат манифеста со списком чанков (.ts)
    
    loop Воспроизведение видео
        FE->>CDN: GET запрос на загрузку видео-чанка (например, chunk_01.ts)
        CDN-->>FE: Возврат бинарных данных чанка
        FE->>User: Отрисовка кадра в видеоплеере
    end
    
    Note over FE, DB: Этап 5: Фоновое сохранение прогресса
    FE->>GW: POST /api/v1/watch-history <br/>{ "movieId": 123, "timestamp": 450 }
    GW->>MS: Сохранение прогресса просмотра
    MS->>DB: UPDATE watch_history SET last_position = 450