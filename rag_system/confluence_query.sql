WITH CommentRank AS (
  SELECT        
    c.page_id,        
    c.created AS comment_created,        
    FORMAT(            
      'Page Comment %d\nCreated On : %s\nCreated By : %s (%s)\n%s\n%s\n%s\n',            
      ROW_NUMBER() OVER(PARTITION BY c.page_id ORDER BY c.created),            
      CAST(c.created AS VARCHAR),            
      u.name,            
      u.email,            
      '-------------------------',            
      c.body,            
      '-------------------------'        
    ) AS formatted_comment    
  FROM        
    confluence.footer_comment c    
  JOIN        
    confluence.footer_comment_version cv ON c.id = cv.footer_comment_id
  JOIN
    confluence.user u ON cv.author_id = u.id
)
SELECT    
  p.id AS page_id,    
  p.title AS page_title,    
  p.created_at AS page_created,    
  pv.page_body AS page_content,
  s.id AS space_id,
  s.name AS space_name,
  FORMAT(        
    '\nPage ID : %d\nCreated On : %s\nTitle : %s\n\n%s',        
    p.id,        
    CAST(p.created_at AS VARCHAR),        
    p.title,        
    LISTAGG(cr.formatted_comment, '\n') WITHIN GROUP (ORDER BY cr.comment_created)    
  ) AS page_details
FROM    
  confluence.page p
LEFT JOIN    
  CommentRank cr ON p.id = cr.page_id
JOIN 
  confluence.page_version pv ON p.id = pv.page_id
JOIN 
  confluence.space s ON p.space_id = s.id
WHERE 
  p.status = 'current'
GROUP BY    
  p.id, p.title, p.created_at, pv.page_body, s.id, s.name;
