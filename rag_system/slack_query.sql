WITH CommentRank AS (
  SELECT        
    m.message_channel_id AS channel_id,        
    m.ts AS comment_created,        
    FORMAT(            
      'Message %s\nTimestamp : %s\nSent By : %s (%s)\n%s\n%s\n%s\n',            
      ROW_NUMBER() OVER(PARTITION BY m.message_channel_id ORDER BY m.ts),            
      CAST(m.ts AS VARCHAR),            
      u.name,            
      u.profile_email,            
      '-------------------------',            
      m.text,            
      '-------------------------'        
    ) AS formatted_comment    
  FROM        
    slack.message m    
  JOIN        
    slack.users u ON m.user_id = u.id
)
SELECT    
  c.id as channel_id,    
  c.name as channel_name,    
  FORMAT(        
    '\nChannel ID : %s\nChannel Name : %s\n\n%s',        
    c.id,        
    c.name,        
    LISTAGG(cr.formatted_comment, '\n') WITHIN GROUP (ORDER BY cr.comment_created)    
  ) AS channel_details
FROM    
  slack.channel c
LEFT JOIN    
  CommentRank cr ON c.id = cr.channel_id
GROUP BY    
  c.id, c.name;
